```json
{
  "id": "16a4928cdf324d40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288604,
  "host_pid": "9e6742732c60:1",
  "hash": "f164ef172ece4c9b966ef9647c1f21141e6bc4e93569387ade8d46bcfa4c0d7c",
  "cid": "QmV1f164ef172ece4c9b966ef9647c1f21141e6bc4e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288604,
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
      "evaluated_at": 1760288604
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
  "sig": "8b20e9f1feebdd8f86a974e98f6257c445963406cbb743e81712ce63fa40c0b4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021718881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 12824574, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285765, 'matching_hash': 'c5f4c03352e0db07'}}}