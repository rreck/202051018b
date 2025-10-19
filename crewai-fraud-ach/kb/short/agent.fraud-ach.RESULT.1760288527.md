```json
{
  "id": "c71a0372de0431fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288527,
  "host_pid": "9e6742732c60:1",
  "hash": "434805f13bab43e840ca9e4a13c13910b3c0339cfcc75c4d7ea06a9c8bb91040",
  "cid": "QmV1434805f13bab43e840ca9e4a13c13910b3c0339c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288527,
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
      "evaluated_at": 1760288527
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
  "sig": "3bc93302093a9c7b53b7c766b6af8fc310c722114806442b5b5a63289d55876f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024591055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 44485152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': '8a72f4eb6bbba5d7'}}}