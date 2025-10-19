```json
{
  "id": "7c7a45f1f4335767",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286535,
  "host_pid": "9e6742732c60:1",
  "hash": "d76a72ea8b971f90cc8bcf001fba3c4979ed0e901defdabb2cd770801747b330",
  "cid": "QmV1d76a72ea8b971f90cc8bcf001fba3c4979ed0e90",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286535,
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
      "evaluated_at": 1760286535
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
  "sig": "c97cf5fcd121c56159a6e9f7a38c5a2a0c6f030b00090b744df7e8aa95aa34d7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009594086126
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285765, 'matching_hash': '58168677024efb84'}}}