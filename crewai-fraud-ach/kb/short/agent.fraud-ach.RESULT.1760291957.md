```json
{
  "id": "38e023a49157b7a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291957,
  "host_pid": "9e6742732c60:1",
  "hash": "a2314703b19ceaefb9404f63204736df3d42d7f2bdcfaad686c1f00610f619ba",
  "cid": "QmV1a2314703b19ceaefb9404f63204736df3d42d7f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291957,
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
      "evaluated_at": 1760291957
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
  "sig": "ca2a6d739ad765e166db03836f9e2824649b540b42c89f681e75691af1ac03a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159207469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 50884570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '9ea174210fc0f6af'}}}