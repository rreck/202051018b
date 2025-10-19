```json
{
  "id": "e65bbda194faa3de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292737,
  "host_pid": "9e6742732c60:1",
  "hash": "e86b0ce26f1a94af5d20a3aebbe274372a961d2d7503bf00dfb918e6ecff5d40",
  "cid": "QmV1e86b0ce26f1a94af5d20a3aebbe274372a961d2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292737,
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
      "evaluated_at": 1760292737
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
  "sig": "6079fc2be2aa6d4f44e87034ac3956a815a77e3033f97b12b9c16c9addef10d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150645649
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 86099424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': 'dd1021bcf813c8ae'}}}