```json
{
  "id": "51a2d6dff31ae1e7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288249,
  "host_pid": "9e6742732c60:1",
  "hash": "673302ba2a5ff202abbd5e2f8247163d66e0c0b1b2e8e15fa1dcc1db1caaaf28",
  "cid": "QmV1673302ba2a5ff202abbd5e2f8247163d66e0c0b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288249,
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
      "evaluated_at": 1760288249
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
  "sig": "fea2c2e267ea2a5549e901e93d05b6e2c95b4dc523767dc6e0524773b064d49e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247533282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 13049826, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285765, 'matching_hash': '15ae64209d1fefcb'}}}