```json
{
  "id": "e9a5ea7a755255fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293505,
  "host_pid": "9e6742732c60:1",
  "hash": "ca30eed705f5d9b73d315c60d1d77dd6338870155e1b21cc5b333a9a22d5f6c8",
  "cid": "QmV1ca30eed705f5d9b73d315c60d1d77dd633887015",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293505,
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
      "evaluated_at": 1760293505
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
  "sig": "7bbdcbb953ed4c1e36db1900fcb930c7484563b3d82555a8517253ceacbec8a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022338434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 98980640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '4c9dfd860457308a'}}}