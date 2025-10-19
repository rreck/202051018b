```json
{
  "id": "5385432aa2abc191",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288696,
  "host_pid": "9e6742732c60:1",
  "hash": "27a9fc573978ca58b257bb1eded622666cdf105ef4f4cd529644e38733554686",
  "cid": "QmV127a9fc573978ca58b257bb1eded622666cdf105e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288696,
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
      "evaluated_at": 1760288696
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
  "sig": "51d5ef3916686869477cf4f03ef204aa4c20b31a0b55a68440afda9257e2e01d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156872006
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': '001baa6337a96952'}}}een': 1760285765, 'matching_hash': 'fa6674ee96d393a2'}}}