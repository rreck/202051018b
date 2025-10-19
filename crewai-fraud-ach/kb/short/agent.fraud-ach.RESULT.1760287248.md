```json
{
  "id": "6547d0732f746a82",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287248,
  "host_pid": "9e6742732c60:1",
  "hash": "b23c7fc55a2ff5aedff64c63e1ca473f275c3450ed661b9b80263ddfa73b806e",
  "cid": "QmV1b23c7fc55a2ff5aedff64c63e1ca473f275c3450",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287248,
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
      "evaluated_at": 1760287248
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "c7f853b94665762655846919313c398e991e9b302082a74379b7069589fe3021"
}
```

Fraud detected: duplicate_transaction (score: 70)
Transaction: 121000246259253
Details: {'velocity': {'fraud_detected': True, 'risk_score': 56, 'details': {'transaction_count': 53, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285765, 'matching_hash': '5582c4cd79a5b751'}}}