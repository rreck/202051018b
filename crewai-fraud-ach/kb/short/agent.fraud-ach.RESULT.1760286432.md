```json
{
  "id": "5cc9db8f9dd9bc01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286432,
  "host_pid": "9e6742732c60:1",
  "hash": "6d7521792955cfceee6dea85ddef243185aab4d607406fb688380e48c3128bde",
  "cid": "QmV16d7521792955cfceee6dea85ddef243185aab4d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286432,
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
      "evaluated_at": 1760286432
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
  "sig": "5e14332dd8225ae46b3b7475f3e00590228c7fe904eb5ad20a5b4e3ec1e867a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026451752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 24915084, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760284979, 'matching_hash': 'ed66d17e763eb837'}}}