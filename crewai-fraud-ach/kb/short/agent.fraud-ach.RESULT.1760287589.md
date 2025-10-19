```json
{
  "id": "bc8ebe25232d8271",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287589,
  "host_pid": "9e6742732c60:1",
  "hash": "5049f0510532382370749c1f44875762fc8a41b6a407d2725f128cca12ab3127",
  "cid": "QmV15049f0510532382370749c1f44875762fc8a41b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287589,
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
      "evaluated_at": 1760287589
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
  "sig": "fbdcf689263e2374a1f5df89d586b61c0fb41d83857925c7c06259f148fd1b5c"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 122105155958228
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 27400230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285765, 'matching_hash': '1e57f627a6d207f5'}}}