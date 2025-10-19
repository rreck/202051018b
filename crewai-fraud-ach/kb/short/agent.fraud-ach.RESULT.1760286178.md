```json
{
  "id": "9116689827c415fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286178,
  "host_pid": "9e6742732c60:1",
  "hash": "2a87f0a1c7edd94309c75733414981d991d232c1c6de0dc7a1bee4de02c7b2ba",
  "cid": "QmV12a87f0a1c7edd94309c75733414981d991d232c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286178,
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
      "evaluated_at": 1760286178
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
  "sig": "64e19b68cbd6d49789dcb959c3c155e97a452d5d2fd73a3bdbed8e9dc79384b3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000029709484
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285763, 'matching_hash': 'f2d4d1f000649e92'}}}