```json
{
  "id": "25d067fafb301ee2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290513,
  "host_pid": "9e6742732c60:1",
  "hash": "5ad9ec24ac9e0cf649c1ddc194938a805fa3d827cc18878b61fd559eb747e76d",
  "cid": "QmV15ad9ec24ac9e0cf649c1ddc194938a805fa3d827",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290513,
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
      "evaluated_at": 1760290513
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
  "sig": "9043373ac0a7901ef2baaf68708a9bf9d6241fcd2f1e8f0cd7b2b341bdb1b30a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021395098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 54845552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': '9c6ceec1730a6176'}}}