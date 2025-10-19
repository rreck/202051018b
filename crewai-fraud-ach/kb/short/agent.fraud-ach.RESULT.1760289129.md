```json
{
  "id": "5a65c8f2108ad45a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289129,
  "host_pid": "9e6742732c60:1",
  "hash": "7cf2dfccc12f8d72789085e7e92b2deb18d8e6f5ccedb686ae995931468464f5",
  "cid": "QmV17cf2dfccc12f8d72789085e7e92b2deb18d8e6f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289129,
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
      "evaluated_at": 1760289129
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
  "sig": "a6db7442a344ad840d1647c8359025c3fa2af2a5deec94ea8400c985fc378233"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157031776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 26447886, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': '2e79bf0e4633df5f'}}}