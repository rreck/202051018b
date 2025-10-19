```json
{
  "id": "9dd66535b9fb15c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288499,
  "host_pid": "9e6742732c60:1",
  "hash": "e5ab1af445f33136279c6855256018db688c1b5f842b824bbde23c7b3df3d27a",
  "cid": "QmV1e5ab1af445f33136279c6855256018db688c1b5f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288499,
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
      "evaluated_at": 1760288499
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
  "sig": "d760b21e6d841e80fef81cc4a05fc8fbe2a37064066451260dc3f2419e8292aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027745016
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 45400595, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285765, 'matching_hash': '88a158c93e7cc45f'}}}