```json
{
  "id": "111559d60aec550d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290080,
  "host_pid": "9e6742732c60:1",
  "hash": "8a5e2cbf11d1c13187738d36bc75cf2d57537d96bfe44714f84db64f78163eaa",
  "cid": "QmV18a5e2cbf11d1c13187738d36bc75cf2d57537d96",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290080,
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
      "evaluated_at": 1760290080
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
  "sig": "1f44d288b0d0475c435e19f3d857f0d28f0ac969c1199e252168afecb4eebf4e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029303857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 36848094, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': '4510d576292a5401'}}}