```json
{
  "id": "cf1308447b9c837e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290747,
  "host_pid": "9e6742732c60:1",
  "hash": "7317175f4612652488e72cadc28a5eb2ff465c7f71af77951f53b64e5e17931f",
  "cid": "QmV17317175f4612652488e72cadc28a5eb2ff465c7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290747,
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
      "evaluated_at": 1760290747
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
  "sig": "2e53c4de4ff8b6822ad18abbf7956de761e72bd959e9fabfe7d689687f49bce7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272135261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 74726496, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760284979, 'matching_hash': 'c71937e0bf846771'}}}