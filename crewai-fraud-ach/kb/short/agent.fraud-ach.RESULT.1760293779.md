```json
{
  "id": "3fa223e1bc12250c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293779,
  "host_pid": "9e6742732c60:1",
  "hash": "272e989650b907f1c11785ae5f75b2d1f6400de7e6176fe11621b9ec65e9d5a6",
  "cid": "QmV1272e989650b907f1c11785ae5f75b2d1f6400de7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293779,
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
      "evaluated_at": 1760293779
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
  "sig": "966f75cf5d3a95ff5695140aea6f8a34d0f68cc1d8a93010f932a8578ba18f06"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 66776625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}