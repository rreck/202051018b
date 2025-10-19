```json
{
  "id": "18599e4aab02eae8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288947,
  "host_pid": "9e6742732c60:1",
  "hash": "7b817f8af7f544cbbbd3cb46c71b13ca88253e86da00040698062a1ae8dcd2e1",
  "cid": "QmV17b817f8af7f544cbbbd3cb46c71b13ca88253e86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288947,
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
      "evaluated_at": 1760288947
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
  "sig": "6ead9893cc1748c4358aaec831e60838a9ccb02709f8d46b7b6d401bf5ef7c0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591752071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 11930268, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285763, 'matching_hash': 'afb8628b94bcbefe'}}}