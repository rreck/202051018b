```json
{
  "id": "ab1d90e79e55438b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288405,
  "host_pid": "9e6742732c60:1",
  "hash": "e293bff7b91887f451bc917012d086fc03170656dbb1d7fcafaaeacea372f66b",
  "cid": "QmV1e293bff7b91887f451bc917012d086fc03170656",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288405,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760288405
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "5d88ee28c41b64ff1919513e673bda76bf6aba12905ff01b0812d0a9722087dc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469103825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 33284588, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285764, 'matching_hash': 'e83bf56ea8077a45'}}}