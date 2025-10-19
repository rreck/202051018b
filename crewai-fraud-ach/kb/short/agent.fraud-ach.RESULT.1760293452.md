```json
{
  "id": "2a7e4bdd15e681c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293452,
  "host_pid": "9e6742732c60:1",
  "hash": "3e0566eb2e698946043c1fcdb7b97cf3d659329b0b455c381d1659533b7099e7",
  "cid": "QmV13e0566eb2e698946043c1fcdb7b97cf3d659329b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293452,
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
      "evaluated_at": 1760293453
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
  "sig": "53befabdc8798da56ce3b7527a33ed7239e1f442f924c7279afa69718caa5452"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467386779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 54750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': 'cfffbd2ec30a8ce4'}}}