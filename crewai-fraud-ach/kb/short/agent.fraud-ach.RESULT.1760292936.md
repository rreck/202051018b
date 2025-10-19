```json
{
  "id": "27174f6cf56deb20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292936,
  "host_pid": "9e6742732c60:1",
  "hash": "28460a47d3ea0828f9231e757f8fd0bcf9bb54b5b21e2752a4dc50cd24807195",
  "cid": "QmV128460a47d3ea0828f9231e757f8fd0bcf9bb54b5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292936,
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
      "evaluated_at": 1760292936
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
  "sig": "0e770abd8bcb2e888a5f4da75b2369cab1dbd9f31b7ba44fde5f675ea4d852bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027363246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 24098048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285764, 'matching_hash': 'ed45becb5b65c89d'}}}