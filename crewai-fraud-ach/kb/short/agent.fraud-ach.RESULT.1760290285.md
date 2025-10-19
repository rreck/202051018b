```json
{
  "id": "fce7b907e70850fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290285,
  "host_pid": "9e6742732c60:1",
  "hash": "4b3c92b772b3389fa43d8fb95dbb6ec489cc8ec07d2aa0f8b77a57bab6b73689",
  "cid": "QmV14b3c92b772b3389fa43d8fb95dbb6ec489cc8ec0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290285,
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
      "evaluated_at": 1760290285
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
  "sig": "f23e22482a1a0c96947f33de4dfb53f109a25e843834e42518e59f73f3546f51"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593456245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 70338858, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285764, 'matching_hash': '5bbbd28055422217'}}}