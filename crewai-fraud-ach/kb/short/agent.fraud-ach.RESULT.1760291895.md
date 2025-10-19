```json
{
  "id": "7cb8cc1caf8567a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291895,
  "host_pid": "9e6742732c60:1",
  "hash": "a062ae2a4ad2d5109e29e22f39c56441e66c55cd9c790b521e389ef22600fe5a",
  "cid": "QmV1a062ae2a4ad2d5109e29e22f39c56441e66c55cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291895,
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
      "evaluated_at": 1760291895
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
  "sig": "b0fb78fcc74acee79fda1e8ec9dfe91d62844e24ce4ed0808f63fddae279ce0f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 58875880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}