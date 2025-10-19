```json
{
  "id": "aab3b824c334c3aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290710,
  "host_pid": "9e6742732c60:1",
  "hash": "d28fddb3b3dab140694250eeff84d110746272a972f55e5877946781ce04a0ab",
  "cid": "QmV1d28fddb3b3dab140694250eeff84d110746272a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290710,
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
      "evaluated_at": 1760290710
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
  "sig": "523dfeda8e4cf5abc996a3a1ed2272b86a04afd673de879e4f01b3ac1979340a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249337095
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 62456641, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285765, 'matching_hash': '2aad7fe43cc5d34d'}}}