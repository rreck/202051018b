```json
{
  "id": "c5085edf6d19c0f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289573,
  "host_pid": "9e6742732c60:1",
  "hash": "5dfa2ecab93737457f203fb64eb04459a0d098245f326b92d40d26750de564ff",
  "cid": "QmV15dfa2ecab93737457f203fb64eb04459a0d09824",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289573,
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
      "evaluated_at": 1760289573
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
  "sig": "f1abf53084107856bf4d4d693ac404ad82ed4946a91f7453bfa3b3e080469c27"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039408811
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285764, 'matching_hash': '99e9efe9af819799'}}}