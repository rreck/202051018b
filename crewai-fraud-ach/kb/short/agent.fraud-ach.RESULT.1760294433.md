```json
{
  "id": "3de83d41726e0e17",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294433,
  "host_pid": "9e6742732c60:1",
  "hash": "5bb6b1b18ba9547633bb8c78c866a6e71db7559098929ea39687106ba2e21153",
  "cid": "QmV15bb6b1b18ba9547633bb8c78c866a6e71db75590",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294433,
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
      "evaluated_at": 1760294433
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
  "sig": "2bb8d8ae0d69def42882ab0b6314f07ba78771fcd5f59d3b095a1fdf2204640c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154543608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 18736312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '3d9c367e54a48e12'}}}