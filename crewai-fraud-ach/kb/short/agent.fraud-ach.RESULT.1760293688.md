```json
{
  "id": "f102d337b7d61718",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293688,
  "host_pid": "9e6742732c60:1",
  "hash": "272c2c798839e96f4ea67a5f2b02b562ba9c0d88435e4292b8fcbb4e6c0725dd",
  "cid": "QmV1272c2c798839e96f4ea67a5f2b02b562ba9c0d88",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293688,
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
      "evaluated_at": 1760293688
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
  "sig": "92b358b6f7a9ee2fe2b5b2d30039d37d44543cc1d58775f48d648684d682d5e5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 55750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285765, 'matching_hash': '9c2417d6ee361cba'}}}