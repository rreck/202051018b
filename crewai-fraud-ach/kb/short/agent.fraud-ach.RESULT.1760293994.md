```json
{
  "id": "91527ee6f5607b17",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293994,
  "host_pid": "9e6742732c60:1",
  "hash": "53fcdb6afa7d24faa786edff4de8dd62e7374e1d656ef6f55d4676eff05460c8",
  "cid": "QmV153fcdb6afa7d24faa786edff4de8dd62e7374e1d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293994,
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
      "evaluated_at": 1760293994
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
  "sig": "984afca95b2b78c62eebb17c7a825b4a1924e46a561025fd6d843f63a1f116b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599169809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 66751668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': '606495659f158f1b'}}}