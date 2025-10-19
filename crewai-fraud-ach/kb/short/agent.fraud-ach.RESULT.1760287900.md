```json
{
  "id": "cd559477d15bd4a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287900,
  "host_pid": "9e6742732c60:1",
  "hash": "d33f7aea1588ceb4721eff963140e0c83637a9f38f12a241628c9a0519a5d2f3",
  "cid": "QmV1d33f7aea1588ceb4721eff963140e0c83637a9f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287900,
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
      "evaluated_at": 1760287900
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
  "sig": "6997823fa710a604085de9c3920f5705991c7673994c98d5bf5467b50963f5c8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468629827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285763, 'matching_hash': 'f998250ed7d87b2f'}}}een': 1760285763, 'matching_hash': '92ff62b724ca331a'}}}