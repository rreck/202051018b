```json
{
  "id": "7f1d8a636583b55a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289636,
  "host_pid": "9e6742732c60:1",
  "hash": "52674353c63831647cd2c9538d1005ed38d2ab3220550a70cd2afee2d4fdff15",
  "cid": "QmV152674353c63831647cd2c9538d1005ed38d2ab32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289636,
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
      "evaluated_at": 1760289636
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
  "sig": "080a30ab692da150bf2c06657e8e3d5781dfa06efd8271089d96792a13b4fe0e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034128514
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 26064837, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285763, 'matching_hash': '342851cb36b9daae'}}}