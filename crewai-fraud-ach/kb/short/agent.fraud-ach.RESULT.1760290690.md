```json
{
  "id": "f93d7edf3a829a84",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290690,
  "host_pid": "9e6742732c60:1",
  "hash": "0247c52c8b4457ded143df868583e4d77056148a9cd2664e1f8a363d43d1f49b",
  "cid": "QmV10247c52c8b4457ded143df868583e4d77056148a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290690,
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
      "evaluated_at": 1760290690
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
  "sig": "d4e876e1f442ad0fbe81b18900e68c4ec88a854a02719d4f67a6a4214a29280b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244267355
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 23606520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '9a2cfa03d6a38585'}}}