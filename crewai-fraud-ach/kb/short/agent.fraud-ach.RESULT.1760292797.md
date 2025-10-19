```json
{
  "id": "4e8ae004b621dd79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292797,
  "host_pid": "9e6742732c60:1",
  "hash": "7e1e3d727c2fc7a5f2bb331921043cbefd0db703e1ca70a8ac5dbf37b25ca618",
  "cid": "QmV17e1e3d727c2fc7a5f2bb331921043cbefd0db703",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292797,
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
      "evaluated_at": 1760292797
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
  "sig": "0fca732fa98a9a11b3d8120e253dc1cfa96318f832d8ed501ae39c3a0de404ba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270009801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 99200115, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': '0a6cdd943232be17'}}}