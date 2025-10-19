```json
{
  "id": "ab64f8e7f7245f60",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289760,
  "host_pid": "9e6742732c60:1",
  "hash": "f511bdce0d12445e57629e27f57cb0155a9155c93a7499a9678abb3a07e615b7",
  "cid": "QmV1f511bdce0d12445e57629e27f57cb0155a9155c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289760,
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
      "evaluated_at": 1760289760
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
  "sig": "36a9f9a472cb4d99cfee3c3e113757ebdcf93c11d8e77350e635d94bdd2d9868"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467867880
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285765, 'matching_hash': 'd47cb9c035f50d52'}}}een': 1760285763, 'matching_hash': '25cb229761d99325'}}}