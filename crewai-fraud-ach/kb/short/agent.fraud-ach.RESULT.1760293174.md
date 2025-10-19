```json
{
  "id": "c7f908ebeb4bd8bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293174,
  "host_pid": "9e6742732c60:1",
  "hash": "051002f951ca4373e55fb4840cc9d9e5ce96b327575f0f2f34c08fe7e756401e",
  "cid": "QmV1051002f951ca4373e55fb4840cc9d9e5ce96b327",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293174,
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
      "evaluated_at": 1760293174
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
  "sig": "5e069a60ee36b7100fa41fdcbaed20b551ebfa32f0c760f7cf999dc39260fa92"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158395869
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 27114474, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '78e23c3ea29c8ae5'}}}