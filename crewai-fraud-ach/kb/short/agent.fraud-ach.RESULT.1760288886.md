```json
{
  "id": "681c94717412d5ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288886,
  "host_pid": "9e6742732c60:1",
  "hash": "7effa75612c9c10abbee5d6fbaca5fa6e1736d2768fe98d53c8ecf4ee101e23c",
  "cid": "QmV17effa75612c9c10abbee5d6fbaca5fa6e1736d27",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288886,
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
      "evaluated_at": 1760288886
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
  "sig": "3afb39e957461e1b32373a733f687b5c462adbb8b32c5344aa4cdbe58403a759"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033129377
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 43045886, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285764, 'matching_hash': '0d940850b17c9224'}}}