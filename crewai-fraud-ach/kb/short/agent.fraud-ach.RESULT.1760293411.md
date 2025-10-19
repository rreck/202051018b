```json
{
  "id": "b7de1dfcbc468053",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293411,
  "host_pid": "9e6742732c60:1",
  "hash": "5926658fe2eb7c51ee8baaecdb8e54e12598d182efab2c4bfa907c8f7baa8968",
  "cid": "QmV15926658fe2eb7c51ee8baaecdb8e54e12598d182",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293411,
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
      "evaluated_at": 1760293411
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
  "sig": "6e0e13189385f5cd11795da6f69ee6dd6fc688c645d7a40e6c65457e561a823e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025664709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 22442446, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285764, 'matching_hash': '5cc83e27ca9ca801'}}}