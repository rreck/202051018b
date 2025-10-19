```json
{
  "id": "8d3f997c1932b4c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293938,
  "host_pid": "9e6742732c60:1",
  "hash": "06baee5d236bab9f75f51901d36179f9269bcf92d2ee5818eb035ed9c44bd058",
  "cid": "QmV106baee5d236bab9f75f51901d36179f9269bcf92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293938,
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
      "evaluated_at": 1760293938
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
  "sig": "816d14b4c551c6833afdaa21b03f41691c2e04b9722259a2fb0ffbf56885f5cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460625527
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 109478760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285765, 'matching_hash': 'd2e448c8360c8b26'}}}