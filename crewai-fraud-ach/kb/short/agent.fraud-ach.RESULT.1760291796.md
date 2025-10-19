```json
{
  "id": "9f5349d6e2e70507",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291796,
  "host_pid": "9e6742732c60:1",
  "hash": "b4fd270bd259e1345801bffdd0c5f61048f8c8ffacf9b780438630722ea7d5f4",
  "cid": "QmV1b4fd270bd259e1345801bffdd0c5f61048f8c8ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291796,
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
      "evaluated_at": 1760291796
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
  "sig": "bbb340e2f9a23a8460383858b3e897817bdbf47fdb37f92ec67a033c8cf3a318"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157447901
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 24745077, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285765, 'matching_hash': '08b33f5611b85fcf'}}}