```json
{
  "id": "cf42f58827227151",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287776,
  "host_pid": "9e6742732c60:1",
  "hash": "2785f7027cb89d17233ce89f5230cea7212052a06c2545f80d819d3dfd84f124",
  "cid": "QmV12785f7027cb89d17233ce89f5230cea7212052a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287776,
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
      "evaluated_at": 1760287776
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
  "sig": "5813791d0553b82c9819428b8c4ec22a550ed21e977d5747784f8a8d4fa228b4"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 063100277559927
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285763, 'matching_hash': '07b51054ae5371fb'}}}