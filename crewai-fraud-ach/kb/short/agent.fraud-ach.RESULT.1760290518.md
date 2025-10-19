```json
{
  "id": "1a033be1df427b1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290518,
  "host_pid": "9e6742732c60:1",
  "hash": "a92249f38e96b3dd713dacfdc578038335c2146275c6c5a8a583350d4fb808e5",
  "cid": "QmV1a92249f38e96b3dd713dacfdc578038335c21462",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290518,
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
      "evaluated_at": 1760290518
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
  "sig": "566bec4bcbf7b6721fa61db2e44484ce79e5ded10cb327d3ff3679d67266d38b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026725963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 30682416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': '729970816697b41b'}}}