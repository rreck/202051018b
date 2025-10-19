```json
{
  "id": "235620319cd631f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290620,
  "host_pid": "9e6742732c60:1",
  "hash": "15a806c291944e80ff4b38010e50dd6c22850bdf5367f9ca928b829c573b2f47",
  "cid": "QmV115a806c291944e80ff4b38010e50dd6c22850bdf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290620,
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
      "evaluated_at": 1760290620
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
  "sig": "aee7fd40f904dfb48d62546eea82fbc3e7846bf378ab0340648390e538890c84"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156823921
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 43326375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': '5764ccd6c01b314b'}}}