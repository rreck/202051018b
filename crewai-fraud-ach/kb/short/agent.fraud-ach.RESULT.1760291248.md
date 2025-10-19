```json
{
  "id": "778934ed62036de8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291248,
  "host_pid": "9e6742732c60:1",
  "hash": "d045411af23139df060b7a95c90411dc7ab9b6df207d70c80f2bd0a26297cb9e",
  "cid": "QmV1d045411af23139df060b7a95c90411dc7ab9b6df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291248,
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
      "evaluated_at": 1760291248
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
  "sig": "2784111b913101809c06c7c03f0c2976699993bef35c882c1696613d4361c985"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022318038
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 40880240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285765, 'matching_hash': 'c47c52aff7a65053'}}}