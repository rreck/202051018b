```json
{
  "id": "c6d06a019d1a3a5d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289362,
  "host_pid": "9e6742732c60:1",
  "hash": "2125c517f7092c0706b09d1c8c4941a1a19118303af2926bad2ad64e9ae4255d",
  "cid": "QmV12125c517f7092c0706b09d1c8c4941a1a1911830",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289362,
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
      "evaluated_at": 1760289362
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
  "sig": "95e01f476882b171e7962a4a25e38a4b4e4372c5fc4021b62c5711ffb3cb2251"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279745557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 11328746, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285765, 'matching_hash': '46b84f4cf2bc4bde'}}}