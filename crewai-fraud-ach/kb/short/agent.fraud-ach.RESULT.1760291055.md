```json
{
  "id": "b1a9bc7e24612a44",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291055,
  "host_pid": "9e6742732c60:1",
  "hash": "5a244c438a5bf5985ad2b079739f97e329c279199de1250c19d593a2b4f3b7c0",
  "cid": "QmV15a244c438a5bf5985ad2b079739f97e329c27919",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291055,
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
      "evaluated_at": 1760291055
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
  "sig": "78707e810c23e0e3eaf94965cddede1be89fb09ec1f6e2b86cb0c22ee300c32f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027960877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 54087448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': '750facc395053d7c'}}}