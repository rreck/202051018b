```json
{
  "id": "755e1175702c643d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293719,
  "host_pid": "9e6742732c60:1",
  "hash": "af7b24174ae1d1d84457c5a9db8264ebdf0f06eac6a79ee5e438ddd794b5b8d7",
  "cid": "QmV1af7b24174ae1d1d84457c5a9db8264ebdf0f06ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293719,
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
      "evaluated_at": 1760293719
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
  "sig": "4ca2bf9a243c1232d99c781e1fbe20e63533af56b074c59ed301718cf48922a0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465310802
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 83779808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': '86dc5261411570c1'}}}}