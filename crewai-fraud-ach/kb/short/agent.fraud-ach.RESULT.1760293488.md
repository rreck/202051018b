```json
{
  "id": "dfff734db912c216",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293488,
  "host_pid": "9e6742732c60:1",
  "hash": "6ded050903b61971f12d6074f7e91418416fd801e98b2896069a0d11acae5da7",
  "cid": "QmV16ded050903b61971f12d6074f7e91418416fd801",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293488,
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
      "evaluated_at": 1760293488
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
  "sig": "5935b13c490a06d7b628c5195d2d9f6fadfb798c3d7753de44cfcbb77c1e429d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023496704
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 74252607, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': 'f379baac52e28232'}}}