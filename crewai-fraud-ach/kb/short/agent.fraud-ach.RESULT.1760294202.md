```json
{
  "id": "e0a1c520215310b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294202,
  "host_pid": "9e6742732c60:1",
  "hash": "25a51e749ffee014cc9dd574ad19d999bbe105e85892e38002b59354e7477c1d",
  "cid": "QmV125a51e749ffee014cc9dd574ad19d999bbe105e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294202,
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
      "evaluated_at": 1760294202
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
  "sig": "78a2472b79dfa450d83232bff6d50d35fd8d31099aa6134ffea915d31a49d59f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593122933
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 94276227, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285765, 'matching_hash': '1a44b34bf830cda9'}}}