```json
{
  "id": "11d6330ea4b2b351",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288882,
  "host_pid": "9e6742732c60:1",
  "hash": "9384419f761d2f76c4f19fde1e2df28682f0db118c9fa6fee48cf4981d149bac",
  "cid": "QmV19384419f761d2f76c4f19fde1e2df28682f0db11",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288882,
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
      "evaluated_at": 1760288882
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
  "sig": "44dd45c8279b8734c4c17cd4aa250a774f5350fd3861dbdf6a9fe76d99a49e24"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270157641
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 38203387, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': 'c979b8e092a32979'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '398958456', 'validation_error': 'Invalid routing number checksum'}}}