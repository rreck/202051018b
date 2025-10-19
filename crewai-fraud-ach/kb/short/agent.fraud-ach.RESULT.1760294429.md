```json
{
  "id": "3a7aec01125dcb29",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294429,
  "host_pid": "9e6742732c60:1",
  "hash": "e288114bd4c425ae53982bcceb49f090ac12c8c813a538fb891753e21364d070",
  "cid": "QmV1e288114bd4c425ae53982bcceb49f090ac12c8c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294429,
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
      "evaluated_at": 1760294430
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
  "sig": "3f24908d45ff09fa9b8078e96b9178bd63f64fae09c886e9ba7b1808483d3267"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033242654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 75862500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '1355ad48790eb31b'}}}