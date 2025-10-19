```json
{
  "id": "5eae3c3c81756dd6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289480,
  "host_pid": "9e6742732c60:1",
  "hash": "f412771abeb12d103c2a4e2df406eb394e6e9a0129b7a3667aa5006f5063b790",
  "cid": "QmV1f412771abeb12d103c2a4e2df406eb394e6e9a01",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289480,
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
      "evaluated_at": 1760289480
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
  "sig": "c600ff9007286414fccb567a94f01a1208bbd3b984d59f9380dbd176754be1bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274395247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 40654020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285765, 'matching_hash': '7ef610f7539e9ec6'}}}