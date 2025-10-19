```json
{
  "id": "55cea04c19835a5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292091,
  "host_pid": "9e6742732c60:1",
  "hash": "1a593895881a5134ef0ca4233fa5090a5132f7b0eb45c2d85a0d20dc29c42846",
  "cid": "QmV11a593895881a5134ef0ca4233fa5090a5132f7b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292091,
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
      "evaluated_at": 1760292091
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
  "sig": "95332560abdec215d7e5d228de987ba78a76538bfb51171ec6360b058939054e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025362322
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 66620650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': '755a8d21dcb7f46a'}}}