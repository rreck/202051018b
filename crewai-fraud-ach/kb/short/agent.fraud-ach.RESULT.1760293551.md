```json
{
  "id": "c759d03c89c74f70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293551,
  "host_pid": "9e6742732c60:1",
  "hash": "96241a1548a975196452f035d2ab7f527eb81199934c01b71a0f16e19ee37be9",
  "cid": "QmV196241a1548a975196452f035d2ab7f527eb81199",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293551,
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
      "evaluated_at": 1760293551
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
  "sig": "a56c905a506d918dd8b0f956d04168ff4e809f6ab07dd4fa6c5ca2c455cdecfa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031517905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 98466771, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'e8f76fb2eb784ea5'}}}