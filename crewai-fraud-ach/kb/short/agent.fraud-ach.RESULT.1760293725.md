```json
{
  "id": "4237fa7cf005da7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293725,
  "host_pid": "9e6742732c60:1",
  "hash": "da426545ec006d90d077b6af0ba67b729c21a156cf3b184cc715b0a3a9009c71",
  "cid": "QmV1da426545ec006d90d077b6af0ba67b729c21a156",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293725,
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
      "evaluated_at": 1760293725
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
  "sig": "b72445bc238b6a09bf0e3310903a20812fd80648ea93e109a9c49af2fa81b30f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276148173
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 63323680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285765, 'matching_hash': 'f15677eba424e05f'}}}