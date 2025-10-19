```json
{
  "id": "16b009f3e3c96a7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288460,
  "host_pid": "9e6742732c60:1",
  "hash": "e474f80046e213ab17f1807c4648123e690e2ca080c84b96125ee52208a38c03",
  "cid": "QmV1e474f80046e213ab17f1807c4648123e690e2ca0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288460,
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
      "evaluated_at": 1760288460
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
  "sig": "de33b3d7ea6cfa8b26f2aab31bbc8fe040bcf92eaca8bc169b0fc981a0df5f7f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591790243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '8c245acd6e70ddc0'}}}een': 1760285764, 'matching_hash': '07aae5a269425bd8'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '098545585', 'validation_error': 'Invalid routing number checksum'}}}